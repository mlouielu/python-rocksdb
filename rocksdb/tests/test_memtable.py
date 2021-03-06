# content of test_sample.py
import rocksdb
import pytest
import shutil
import os


def clean_db():
    if os.path.exists('/tmp/test'):
        shutil.rmtree("/tmp/test")

def test_open_skiplist_memtable_factory():
    clean_db()
    opts = rocksdb.Options()
    opts.memtable_factory = rocksdb.SkipListMemtableFactory()
    opts.create_if_missing = True
    test_db = rocksdb.DB("/tmp/test", opts)

def test_open_vector_memtable_factory():
    clean_db()
    opts = rocksdb.Options()
    opts.allow_concurrent_memtable_write = False
    opts.memtable_factory = rocksdb.VectorMemtableFactory()
    opts.create_if_missing = True
    test_db = rocksdb.DB("/tmp/test", opts)
