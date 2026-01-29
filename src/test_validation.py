import re
from typing import Tuple

# COPIED FROM src/agent/tools.py (Lines 185-223)
def validate_bullet_preservation(original: str, tailored: str, section_name: str) -> Tuple[bool, str]:
    """
    Validate that tailored bullet preserves critical elements from original.
    
    Focus on preserving:
    - Numbers, metrics, percentages (MUST be preserved)
    - Company names (MUST be preserved)
    
    Note: Technologies can be selectively removed if they don't contribute to ATS.
    
    Args:
        original: Original bullet text
        tailored: Tailored bullet text
        section_name: Name of section for error reporting
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Extract all numbers (including percentages, decimals, and counts)
    # These MUST be preserved - no changes allowed
    number_pattern = r'\d+(?:[.,]\d+)?%?(?:\+)?'
    original_numbers = set(re.findall(number_pattern, original))
    tailored_numbers = set(re.findall(number_pattern, tailored))
    
    missing_numbers = original_numbers - tailored_numbers
    if missing_numbers:
        return False, f"{section_name}: Missing numbers/metrics: {missing_numbers}"
    
    # Check for company/institution names (these MUST be preserved)
    company_keywords = ['Brandl', 'Nutrition', 'Braunschweig', 'SciBiome', 'TECHR', 'TU']
    for keyword in company_keywords:
        if keyword in original and keyword not in tailored:
            return False, f"{section_name}: Missing company/institution name: {keyword}"
    
    # Note: We no longer strictly validate technologies since agent can
    # remove non-ATS-contributing details. The agent is responsible for
    # only removing filler, not core technologies.
    
    return True, ""

# TEST DRIVER
def test_bullet(original, tailored, name):
    print(f"\n--- Test: {name} ---")
    print(f"Original: {original}")
    print(f"Tailored: {tailored}")
    
    valid, error = validate_bullet_preservation(original, tailored, name)
    
    if valid:
        print("RESULT: ✅ PASS")
    else:
        print(f"RESULT: ❌ FAIL - {error}")
    return valid

if __name__ == "__main__":
    print("Running Verification for Surgical Edits (Isolated Test)...")

    # Test 1: Surgical Insertion (Valid)
    # User's example: Adding "production-ready", "numpy", "ML pipeline"
    o1 = "Built general-purpose image enhancement pipeline combining KBNets denoising with Real-ESRGAN 4K upscaling using PyTorch and OpenCV"
    t1 = "Engineered production-ready image enhancement ML pipeline combining KBNets denoising with Real-ESRGAN 4K upscaling using PyTorch, OpenCV, and numpy, for scalable computer vision application"
    test_bullet(o1, t1, "User Example: Image Enhancement")

    # Test 2: Surgical Insertion (Valid - Simple)
    o2 = "Built forecasting system"
    t2 = "Built production-grade forecasting system using Prophet"
    test_bullet(o2, t2, "Simple Insertion")

    # Test 3: Invalid - Removed Metric
    o3 = "Reduced latency by 50%"
    t3 = "Reduced latency significantly"
    test_bullet(o3, t3, "Removed Metric (Should Fail)")

    # Test 4: Invalid - Changed Metric
    o4 = "Managed 5-person team"
    t4 = "Managed 10-person team"
    test_bullet(o4, t4, "Changed Metric (Should Fail)")
    
    # Test 5: Company Name Preservation
    o5 = "Worked at Brandl Nutrition"
    t5 = "Worked at BN startup"
    test_bullet(o5, t5, "Removed Company Name (Should Fail)")
