#!/usr/bin/env python3
"""
Query weather information for a given location using OpenAI API.
"""

import os
import sys
from openai import OpenAI


def get_weather(location: str) -> str:
    """
    Query weather information for a given location using OpenAI API.
    
    Args:
        location: The location to query weather