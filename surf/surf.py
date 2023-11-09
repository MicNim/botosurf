#!/usr/bin/env python3
"""
Surf Class
"""

import boto3
from logzero import logger

class Surf():
  """Class to collect AWS services."""
  def __init__(self, session, service='s3') -> None:
    self._all_methods = []
    self._all_services = session.get_available_services()
    self._client = boto3.client(service)
    self._service = service  
  
  @property
  def all_methods(self):
    return self._all_methods
  
  @property
  def all_services(self):
    return self._all_services

  @property
  def client(self):
    return self._client

  @property
  def service(self):
    return self._service

  @service.setter
  def service(self, service):
    logger.info("updating service client...")
    self._service = service
    self._client = boto3.client(service)

    methods = [x for x in dir(self.client) if not x.startswith(('_', '__'))] 

    self._all_methods = methods