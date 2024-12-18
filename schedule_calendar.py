import asyncio
import time
from src.client import client

async def main():

    workflow_id = f"{int(time.time() * 1000)}-GreetingWorkflow"
    await client.schedule_workflow(
        workflow_name="GreetingWorkflow",
        workflow_id=workflow_id,
        schedule=ScheduleSpec(
            calendars=[ScheduleCalendarSpec(
                day_of_week=[ScheduleRange(start=1)],
                hour=[ScheduleRange(start=9)]
            )]
        )
    )

    exit(0)

def run_schedule_calendar():
    asyncio.run(main())

if __name__ == "__main__":
    run_schedule_calendar()