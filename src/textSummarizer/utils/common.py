import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads the yaml file and returns a ConfigBox
       Args:
            path_to_yaml: Path like input
       Raises:
            ValueError: if path_to_yaml is empty
            e: empty yaml file
            
       Returns:
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml+file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations

def create_directories(path_to_directories:list, verbose = True):
    """Create list of directories
    Args:
         path_to_directories(list): list of directories
         ignore_log (bool, optional): ignore if multiple directories is to be created ...defaults to false
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"creating directory at: {path}")




@ensure_annotations_

def get_size(path: Path) -> str:
    """get size in KB
    Args:
         path (Path): path of the file
         
    Returns:
         str: size in KB


    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
