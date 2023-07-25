import os, sys

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        self.error_message = CustomException
        pass

    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str:
        _, _, exce_tb = error_details.exc_info()
        
        exception_block_line_numer = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename
        

