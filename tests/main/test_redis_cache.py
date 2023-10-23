import pytest

from langroid.cachedb.redis_cachedb import RedisCache, RedisCacheConfig


@pytest.fixture
def fake_redis_cache():
    config = RedisCacheConfig(fake=True)
    return RedisCache(config=config)


@pytest.mark.unit
def test_fake_store_and_retrieve(fake_redis_cache):
    key = "test_key"
    data = {"info": "something"}
    fake_redis_cache.store(key, data)
    result = fake_redis_cache.retrieve(key)
    assert result == data


@pytest.fixture
def real_redis_cache():
    config = RedisCacheConfig(
        fake=False,
        hostname="redis-11524.c251.east-us-mz.azure.cloud.redislabs.com",
        port=11524,
    )
    return RedisCache(config=config)


@pytest.mark.integration
def test_real_store_and_retrieve(real_redis_cache):
    key = "test_key"
    data = {"info": "something"}
    real_redis_cache.store(key, data)
    result = real_redis_cache.retrieve(key)
    assert result == data
