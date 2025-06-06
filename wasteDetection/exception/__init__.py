import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # May raise AttributeError if exc_tb is None
    error_message = "Error occurred in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class AppException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: Original error or exception instance
        :param error_detail: Typically 'sys' to extract exception context
        """
        super().__init__(str(error_message))  # Ensure consistency in base exception
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
