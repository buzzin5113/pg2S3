"""
PostgreSQL to Amazon S3
"""
import boto3
import subprocess


def createbackup():
    command = 'pg_basebackup -X fetch --format=t -D - | bzip2 -9 > ~/backup-psql-$(date +%Y-%m-%d-%H-%M).tar.bz2';
    with subprocess.Popen([command], stdout=subprocess.PIPE) as proc:
        log.write(proc.stdout.read())


def main():
    createbackup()


if __name__ == "__main__":
    main()
