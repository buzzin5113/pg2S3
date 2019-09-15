"""
PostgreSQL to Amazon S3
"""
import boto3
import subprocess


def createbackup():
    command = 'pg_basebackup -h localhost -D ~/backup/';
    with subprocess.popen([command], stdout=PIPE) as proc:
        log.write(proc.stdout.read())


def main():
    createbackup()


if __name__ == "__main__":
    main()
