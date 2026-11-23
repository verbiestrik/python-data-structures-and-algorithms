"""
HTML Tag Matching
=================

Problem:
    Check whether the opening and closing HTML tags in a source string
    are correctly matched and nested.

Approach:
    - Use the implemented ArrayStack (in data_structures) to keep track of opening tags.
    - Scan the source string to identify HTML tags.
    - Extract tag names independently of their attributes.
    - Convert tag names to lowercase because HTML tag names are case-insensitive.
    - Push opening tags onto the stack.
    - When encountering a closing tag, check whether the stack is empty.
      If it is not, pop the most recently opened tag and compare the names.
    - Ignore self-closing tags and HTML void elements, which do not require
      closing tags.
    - Ignore HTML comments, declarations and processing instructions.
    - Treat the contents of raw-text elements (e.g. script and style) as text.
    - Return True if all tags are correctly matched and the stack is empty.

    This implementation checks tag nesting but is not a complete HTML
    validator. It does not validate attribute syntax, optional closing tags
    or all HTML5 parsing rules.

Time Complexity:
    - O(n), where n is the length of the HTML source string.
      Each part of the source is scanned a constant number of times.

Space Complexity:
    - O(d), where d is the maximum nesting depth of HTML elements.
      The ArrayStack stores at most one reference per unmatched opening tag.

Python Alternatives:
    - html.parser.HTMLParser provides standard-library HTML parsing
      functionality, but does not independently enforce correct tag nesting.
    - xml.etree.ElementTree can be used for well-formed XML/XHTML documents,
      but is not a general-purpose HTML parser.
"""

from data_structures.stacks.array_stack import ArrayStack

def match_html(html_src):
    """Return True if all opening and closing HTML tags match."""
    if not isinstance(html_src, str):
        raise TypeError("HTML source must be a string")

    stack = ArrayStack()
    j = html_src.find('<')

    while j != -1:
        k = html_src.find('>', j + 1)

        if k == -1:
            return False

        tag = html_src[j + 1:k]

        if not tag:
            return False

        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty() or stack.pop() != tag[1:]:
                return False

        j = html_src.find('<', k + 1)

    return stack.is_empty()
