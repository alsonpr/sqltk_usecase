from src.sqltk.orchestrator import Orchestrator
from settings import *

orchestrator = {
    "db_info": DB_INFO,
    "language": language,
    "report_output_path": report_output_path,
    "element_to_search_path": element_to_search_path,
    "input_query_path_list": input_query_path_list,
    "validation_test_list": validation_test_list,
    "report_output_format": report_output_format,
    "solution_query_path": solution_query_path

}

obj1 = Orchestrator(orchestrator)
obj1.generate_report()
