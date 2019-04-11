from fabric.api import abort, cd, env, local, run, task


env.use_ssh_config = True
env.hosts = ["webfaction"]
env.remote_app_dir = '/home/paloni/webapps/horizons/'
env.remote_apache_dir = '/home/paloni/webapps/horizons/apache2/bin/'


@task
def deploy():
    local("git push origin HEAD")
    with cd(f'{env.remote_app_dir}'):
        run('git pull origin master')
        run('/home/paloni/.local/share/virtualenvs/horizons-1jRzT3a9/bin/activate')
        run('pipenv install')

    run(f'cd {env.remote_apache_dir}; touch wsgi.py;')
