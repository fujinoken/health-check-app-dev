# -*- coding: utf-8 -*-
def test_runtime_import():
    import services.runtime
    assert services.runtime is not None
