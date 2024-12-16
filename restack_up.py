import os
from restack_sdk_cloud import RestackCloud
from dotenv import load_dotenv
load_dotenv(override=True)

print(f"GIT_URL: {os.getenv('GIT_URL')}")
print(f"GIT_BRANCH: {os.getenv('GIT_BRANCH')}")

async def main():
    # Initialize the RestackCloud client with the SDK token from environment variables
    restack_cloud_client = RestackCloud(os.getenv('RESTACK_CLOUD_TOKEN'))
    git_url = os.getenv('GIT_URL', 'default_git_url')
    git_branch = os.getenv('GIT_BRANCH', 'default_git_branch')
    print("git_url: ", git_url)
    print("git_branch: ", git_branch)


    engine = {
        'name': 'restack_engine', # IMPORTANT: This must match the name of the engine in the Restack Cloud console.
        'image': 'ghcr.io/restackio/restack:main',
        'portMapping': [
            {
                'port': 5233,
                'path': '/',
                'name': 'engine-frontend',
            },
            {
                'port': 6233,
                'path': '/api',
                'name': 'engine-api',
            }
        ],
        'environmentVariables': [
          {
              'name': 'RESTACK_ENGINE_ID',
              'value': os.getenv('RESTACK_ENGINE_ID'),
          },
          {
              'name': 'RESTACK_ENGINE_ADDRESS',
              'value': os.getenv('RESTACK_ENGINE_ADDRESS'),
          },
          {
              'name': 'RESTACK_ENGINE_API_KEY',
              'value': os.getenv('RESTACK_ENGINE_API_KEY'),
          },
          {'name': 'gitUrl', 'value': os.getenv('GIT_URL')},
          {'name': 'gitBranch', 'value': os.getenv('GIT_BRANCH')}
        ],
        'gitUrl': os.getenv('GIT_URL'),
        'gitBranch': os.getenv('GIT_BRANCH'),
    }

    # Define the application configuration
    app = {
        'name': 'defense_quickstart',
        'dockerFilePath': '/examples/defense_quickstart/Dockerfile',
        'dockerBuildContext': './examples/defense_quickstart/',
        'gitUrl': git_url,
        'gitBranch': git_branch,
        'environmentVariables': [
            {
                'name': 'RESTACK_ENGINE_ID',
                'value': os.getenv('RESTACK_ENGINE_ID'),
            },
            {
                'name': 'RESTACK_ENGINE_ADDRESS',
                'value': os.getenv('RESTACK_ENGINE_ADDRESS'),
            },
            {
                'name': 'RESTACK_ENGINE_API_KEY',
                'value': os.getenv('RESTACK_ENGINE_API_KEY'),
            },
            {
                'name': 'OPENBABYLON_API_URL',
                'value': os.getenv('OPENBABYLON_API_URL', ''),
            },
            {'name': 'gitUrl', 'value': os.getenv('GIT_URL')},
            {'name': 'gitBranch', 'value': os.getenv('GIT_BRANCH')}
        ],
    'gitUrl': os.getenv('GIT_URL'),
    'gitBranch': os.getenv('GIT_BRANCH'),
    }

    # Configure the stack with the applications
    await restack_cloud_client.stack({
        'name': 'development environment python',
        'previewEnabled': False,
        'applications': [engine,app],
    })

    # Deploy the stack
    await restack_cloud_client.up()

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
