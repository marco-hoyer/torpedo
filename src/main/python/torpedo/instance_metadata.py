import requests
import functools
from urllib.parse import urljoin

INSTANCE_METADATA_API_BASE_URL = "http://169.254.169.254/latest/"
METADATA_BASE_URL = urljoin(INSTANCE_METADATA_API_BASE_URL, "meta-data/")

__cache = {}


def cached(f):
    @functools.wraps(f)
    def with_caching(*args, **kwargs):
        name = f.__name__
        if name in __cache:
            return __cache[name]
        result = f(*args, **kwargs)
        __cache[name] = result
        return result

    return with_caching


@cached
def ami_id():
    return requests.get(urljoin(METADATA_BASE_URL, "ami-id")).content.decode('utf-8')


@cached
def ami_launch_index():
    return requests.get(urljoin(METADATA_BASE_URL, "ami-launch-index")).content.decode('utf-8')


@cached
def ami_manifest_path():
    return requests.get(urljoin(METADATA_BASE_URL, "ami-manifest-path")).content.decode('utf-8')


@cached
def availability_zone():
    return requests.get(urljoin(METADATA_BASE_URL, "placement/availability-zone")).content.decode('utf-8')


@cached
def hostname():
    return requests.get(urljoin(METADATA_BASE_URL, "hostname")).content.decode('utf-8')


@cached
def instance_action():
    return requests.get(urljoin(METADATA_BASE_URL, "instance-action")).content.decode('utf-8')


@cached
def instance_id():
    return requests.get(urljoin(METADATA_BASE_URL, "instance-id")).content.decode('utf-8')


@cached
def instance_type():
    return requests.get(urljoin(METADATA_BASE_URL, "instance-type")).content.decode('utf-8')


@cached
def kernel_id():
    return requests.get(urljoin(METADATA_BASE_URL, "kernel-id")).content.decode('utf-8')


@cached
def local_hostname():
    return requests.get(urljoin(METADATA_BASE_URL, "local-hostname")).content.decode('utf-8')


@cached
def local_ipv4():
    return requests.get(urljoin(METADATA_BASE_URL, "local-ipv4")).content.decode('utf-8')


@cached
def mac():
    return requests.get(urljoin(METADATA_BASE_URL, "mac")).content.decode('utf-8')


@cached
def public_hostname():
    return requests.get(urljoin(METADATA_BASE_URL, "public-hostname")).content.decode('utf-8')


@cached
def public_ipv4():
    return requests.get(urljoin(METADATA_BASE_URL, "public-ipv4")).content.decode('utf-8')


@cached
def reservation_id():
    return requests.get(urljoin(METADATA_BASE_URL, "reservation-id")).content.decode('utf-8')


@cached
def security_groups():
    return requests.get(urljoin(METADATA_BASE_URL, "security-groups")).content.decode('utf-8')


@cached
def user_data():
    return requests.get(urljoin(INSTANCE_METADATA_API_BASE_URL, "user-data")).content.decode('utf-8')
