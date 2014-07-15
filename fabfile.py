from fabric.api import *


try:
    import config
    env.user= config.USERNAME
    env.password= config.PASSWORD
    nodes= config.NODES
    env.hosts=[x for x in nodes.values()]
except ImportError:
    print "Check config.py file"

def clone_webqa_credentials():
    run("hostname")
    with cd("/home/webqa/"):
        run("git clone git@github.com:mozilla/webqa-credentials")

def check_webqa_credentials_commits():
    run("hostname")
    with cd ("/home/webqa/webqa-credentials"):
        run("git log -1 --no-merges")

def update_webqa_credentials():
    run("hostname")
    with cd("/home/webqa/webqa-credentials"):
        run("git pull origin master")

def install_git():
    run("hostname")
    sudo("apt-get install git -y")

def install_java_and_adb():
    run("hostname")
    sudo("add-apt-repository  ppa:webupd8team/java -y")
    sudo("add-apt-repository ppa:nilarimogard/webupd8 -y")
    sudo("apt-get update")
    sudo("apt-get install mutt oracle-java8-installer -y")
    sudo("apt-get install android-tools-adb android-tools-fastboot -y")

def install_python():
    run("hostname")
    sudo("apt-get install python-pip mutt python-dev vim libbluetooth-dev -y")
    sudo("pip install virtualenv")

def create_jenkins_dir():
    run("hostname")
    sudo("mkdir /var/jenkins")
    sudo("chmod -R /var/jenkins/")

def create_node_dir():
    run("hostname")
    with cd("/var/jenkins"):
        run("mkdir 1")
        run("mkdir 2")
