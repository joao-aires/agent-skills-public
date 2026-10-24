"""Synthetic repository evidence: standard-library lookup service, no model calls."""
import json
from http.server import BaseHTTPRequestHandler

DOCUMENTS = {
    "doc-7": {"id": "doc-7", "title": "Example document", "text": "A supported fact."}
}


def lookup_document(document_id):
    record = DOCUMENTS.get(document_id)
    if record is None:
        return None
    return {key: record[key] for key in ("id", "title", "text")}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/documents/lookup":
            self.send_error(404)
            return
        try:
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            record = lookup_document(body["documentId"])
        except (ValueError, KeyError):
            self.send_error(400)
            return
        if record is None:
            self.send_error(404)
            return
        encoded = json.dumps(record).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
