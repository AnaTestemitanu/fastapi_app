import pytest
from aioresponses import aioresponses
from app.utils.data_fetcher import fetch_data

# Test case for successful data fetching
@pytest.mark.asyncio
async def test_fetch_data_success():
    # aioresponses to mock the HTTP request and response
    with aioresponses() as m:
        # Mock the response with a successful payload
        m.get('https://jsonplaceholder.typicode.com/posts', payload={'data': 'success'})
        
        # Call the fetch_data function with the mocked URL
        response = await fetch_data('https://jsonplaceholder.typicode.com/posts')
        
        # Assert that the response matches the expected payload
        assert response == {'data': 'success'}


# Test case for data fetching with retry
@pytest.mark.asyncio
async def test_fetch_data_with_retry():
    # aioresponses to mock the HTTP request and response
    with aioresponses() as m:
        # Simulate a 500 response on the first attempt
        m.get('https://jsonplaceholder.typicode.com/posts', status=500)
        # Simulate a successful response on the second attempt
        m.get('https://jsonplaceholder.typicode.com/posts', payload={'data': 'success'}, status=200)
        
        # Call the fetch_data function which should retry on failure
        result = await fetch_data('https://jsonplaceholder.typicode.com/posts')
        
        # Assert that the result matches the successful payload
        assert result == {'data': 'success'}
