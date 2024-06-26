# Import
from typing import *

import sqlalchemy as sa
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import AutomapBase, automap_base

__engines: Dict[str, MockConnection] = dict()
databases: Dict[str, AutomapBase] = dict()
sessions: Dict[str, Session] = dict()


def global_init(db_files: List[str]):
    """Invokes `engine_init`, `database_init`, `sessions_init` with pre-defined value `db_names` (global_declarations.py)."""

    engines_init(db_files)

    names = list(__engines.keys())

    databases_init(names)
    sessions_init(names)


def engines_init(db_files: List[str]) -> None:
    """Initializes all engines. Other functions (except for `global_init`) won't work without it."""

    global __engines

    if not db_files:
        raise NameError("No db files found")

    for db_file in db_files:
        database_name = f"sqlite:///{db_file}?check_same_thread=False"

        name = db_file.split("\\")[-1].split(".")[0]

        __engines[name] = sa.create_engine(database_name)


def databases_init(db_names: List[str]):
    """Initializes all databases."""

    global databases

    for name in db_names:
        metadata = sa.MetaData()
        metadata.reflect(__engines[name])

        databases[name] = automap_base(metadata=metadata)
        databases[name].prepare()
        databases[name].metadata.create_all(__engines[name])


def sessions_init(db_names: List[str]):
    """Initializes all sessions."""

    global sessions

    for name in db_names:
        sessions[name] = Session(__engines[name])
