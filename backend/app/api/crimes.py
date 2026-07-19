from fastapi import APIRouter

router = APIRouter()

@router.get('/stats')
async def stats():
    # Return sample statistics
    return {
        "total_crimes": 12345,
        "todays_cases": 12,
        "active_investigations": 45
    }
