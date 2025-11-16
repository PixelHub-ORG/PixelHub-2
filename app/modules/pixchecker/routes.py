from flask import jsonify
import re

from app.modules.pixchecker import pixchecker_bp
from app.modules.hubfile.services import HubfileService


@pixchecker_bp.route('/pixchecker/check_pix/<int:file_id>', methods=['GET'])
def check_pix(file_id):
    """Validate a simple PIX-like file syntax.

    Expected structure:
    element1{
        attr1=val1
        attr2=val2
    }
    element2{
        ...
    }

    Returns JSON with 200 on success, or 400 with a list of errors.
    """
    try:
        hubfile = HubfileService().get_or_404(file_id)
        path = hubfile.get_path()

        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()

        errors = []

        # Allow either unquoted identifiers (letters, digits, underscore, dash)
        # or quoted strings (single or double) which may include spaces.
        element_header_re = re.compile(r"^\s*(?:\"([^\"]+)\"|'([^']+)'|([A-Za-z_][\w\-]*))\s*\{\s*$")
        # For attributes: key can be quoted or unquoted, value is the rest (non-empty, trimmed)
        attr_re = re.compile(r"^\s*(?:\"([^\"]+)\"|'([^']+)'|([A-Za-z_][\w\-]*))\s*:\s*(\S(?:.*\S)?)\s*$")

        state = "outside"  # or "inside"
        current_element = None

        for idx, raw in enumerate(lines, start=1):
            line = raw.rstrip('\n')
            if state == "outside":
                if line.strip() == "":
                    continue
                m = element_header_re.match(line)
                if m:
                    # group(1) -> double-quoted name, group(2) -> single-quoted name,
                    # group(3) -> unquoted identifier
                    current_element = m.group(1) or m.group(2) or m.group(3)
                    state = "inside"
                else:
                    errors.append(f"Line {idx}: Expected element header like 'name{{' but got: {line!r}")
            else:  # inside an element
                stripped = line.strip()
                if stripped == "":
                    continue
                if stripped == "}":
                    current_element = None
                    state = "outside"
                    continue

                # attribute line expected
                m = attr_re.match(line)
                if m:
                    # key: group(1) double-quoted, group(2) single-quoted, group(3) unquoted
                    value = m.group(4)
                    # a simple additional check: value should not contain braces
                    if "{" in value or "}" in value:
                        errors.append(f"Line {idx}: Attribute value must not contain '{{' or '}}': {line!r}")
                else:
                    if "{" in line:
                        errors.append(f"Line {idx}: Unexpected '{{' inside element {current_element!r}")
                    else:
                        errors.append(f"Line {idx}: Invalid attribute format, expected 'key=value', got: {line!r}")

        if state == "inside":
            errors.append(f"Unexpected end of file: missing closing '}}' for element {current_element!r}")

        if errors:
            return jsonify({"errors": errors}), 400

        return jsonify({"message": "Valid Model"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@pixchecker_bp.route('/pixchecker/valid/<int:file_id>', methods=['GET'])
def valid(file_id):
    return jsonify({"success": True, "file_id": file_id})