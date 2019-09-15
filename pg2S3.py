"""
PostgreSQL to Amazon S3
"""
import boto3
import subprocess


def createbackup():
    command = ['/usr/bin/pg_basebackup', ' -X fetch --format=t -D -'];
    ps =  subprocess.Popen(command, stdout=subprocess.PIPE)
    output = subprocess.check_output(('bzip2', ' -9 > ~/backup-psql-$(date +%Y-%m-%d-%H-%M).tar.bz2'), stdin=ps.stdout)
    ps.wait()

def main():
    createbackup()


if __name__ == "__main__":
    main()
