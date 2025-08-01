"""Define the configurable parameters for the agent."""

import os
from dataclasses import dataclass, field, fields
from typing import Any, Optional

from langchain_core.runnables import RunnableConfig
from typing_extensions import Annotated

from src.agent import prompts


@dataclass(kw_only=True)
class Configuration:
    """Main configuration class for the memory graph system."""

    user_id: str = "default"
    """The ID of the user to remember in the conversation."""

    model: str = field(
        default="gemini-2.5-flash",
        metadata={
            "description": "The name of the language model to use for the agent. "
            "Should be in the form: model-name."
        },
    )

    model_provider:  str = field(
        default="google_genai",
        metadata={
            "description": "The name of the language model to use for the agent. "
            "Should be in the form: provider-name"
        },
    )
    
    system_prompt: str = prompts.SYSTEM_PROMPT

    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        configurable = (
            config["configurable"] if config and "configurable" in config else {}
        )
        values: dict[str, Any] = {
            f.name: os.environ.get(f.name.upper(), configurable.get(f.name))
            for f in fields(cls)
            if f.init
        }

        return cls(**{k: v for k, v in values.items() if v})