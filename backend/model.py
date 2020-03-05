class Data:
    def __init__(self, summary="", url=""):
        self._summary= summary;
        self._url = url;

        # getter method

    def get_summary(self):
        return self._summary

        # setter method

    def set_summary(self, x):
        self._summary = x

    def get_url(self):
        return self._url

        # setter method

    def set_url(self, x):
        self._url = x