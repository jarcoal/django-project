import json

from django.conf import settings
from newrelic.agent import NewRelicContextFormatter
from rest_framework.utils.encoders import JSONEncoder

INDENT = 4 if settings.ENVIRONMENT == "local" else None


class JsonFormatter(NewRelicContextFormatter):
    """Custom JSON log formatter that adds New Relic tracing attributes to output."""

    def format(self, record):
        record_as_dict = self.log_record_to_dict(record)

        # NewRelicContextFormatter calls record.getMessage() when generating
        # the "message" key, which tries to convert the message object to a
        # string.  We replace it with the original message so that it's
        # encoded properly.
        record_as_dict["message"] = record.msg

        return json.dumps(record_as_dict, cls=JSONEncoder, indent=INDENT)
