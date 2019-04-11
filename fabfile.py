from fabric.api import abort, cd, env, local, run, task


env.use_ssh_config = True
env.hosts = ["webfaction"]
env.remote_app_dir = '/home/paloni/webapps/horizons/'


@task
def deploy():
    local("git push origin HEAD")
    with cd(f'{env.remote_app_dir}'):
        run('git pull origin master')

    run(f'cd {env.remote_app_dir}/project/; touch wsgi.py;')
