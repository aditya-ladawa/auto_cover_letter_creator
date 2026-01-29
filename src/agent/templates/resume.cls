%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Medium Length Professional CV - RESUME CLASS FILE
%
% This class file defines the structure and design of the template.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[2024/01/01 Resume class]

\LoadClass[11pt,letterpaper]{article}

\usepackage[parfill]{parskip}
\usepackage{array}
\usepackage{ifthen}
\usepackage{hyperref}
\usepackage{enumitem}

% Configure hyperlinks to be blue
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue
}

\pagestyle{empty}
\raggedbottom


%----------------------------------------------------------------------------------------
%	HEADINGS COMMANDS
%----------------------------------------------------------------------------------------

\def \name#1{\def\@name{#1}}
\def \@name {}

\def \address#1{\def\@addressone{#1}}
\def \@addressone {}

\def \printname {
  \begingroup
    \hfil{\MakeUppercase{\namesize\bf \@name}}\hfil
    \nameskip\break
  \endgroup
}

\def \printaddress #1{
  \begingroup
    \centerline{#1}
  \endgroup
  \par
  \addressskip
}

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document
  \printname
  \@ifundefined{@addressone}{}{\printaddress{\@addressone}}
}

%----------------------------------------------------------------------------------------
%	SECTION FORMATTING
%----------------------------------------------------------------------------------------

\newenvironment{rSection}[1]{
  \sectionskip
  \MakeUppercase{\bf #1}
  \sectionlineskip
  \hrule
  \begin{list}{}{
    \setlength{\leftmargin}{0em}
    \setlength{\itemsep}{0em}
    \setlength{\parsep}{0em}
    \setlength{\topsep}{0em}
    \setlength{\partopsep}{0em}
  }
  \item[]
}{
  \end{list}
}

%----------------------------------------------------------------------------------------
%	SIZE DEFINITIONS
%----------------------------------------------------------------------------------------

\def\namesize{\huge}
\def\nameskip{\bigskip}
\def\addressskip{\smallskip}
\def\sectionskip{\medskip}
\def\sectionlineskip{\medskip}

% Slightly increase spacing between bullet points
\setlist[itemize]{itemsep=0.3em, topsep=0.2em}
