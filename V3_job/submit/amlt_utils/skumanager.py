#!/usr/bin/env python -u
# -*- coding: utf-8 -*-

# Copyright  2020  Microsoft (author: Ke Wang)

from __future__ import absolute_import, division, print_function


def get_premium_storage_by_cluster_name(cluster_name, region=None):
    """get associated storage account for a cluster"""

    cluster_storage_dict = {
        "a100-80gb-eus2":   "exawattaiprmbtts01eus",
        "itp-p40-eus-01":   "exawattaiprmbtts01eus",
        "v100-16gb-scus":   "exawattaiprmbtts01scus",
        "a100-scus":        "exawattaiprmbtts01scus",
        "itp-v100-scus":    "exawattaiprmbtts01scus",
        "itp-v100-scus-2":  "exawattaiprmbtts01scus",
        "itp-p100-wus2":    "exawattaiprmbtts01wus2",
        "v100-32gb-wus2-2": "exawattaiprmbtts01wus2",
        "a100-80gb-wus3":   "exawattaiprmbtts01wus2",
        "a100-8x-wus2":     "exawattaiprmbtts01wus2",  # ITP team"s cluster
    }

    region_storage_dict = {
        "eastus":         "exawattaiprmbtts01eus",
        "southcentralus": "exawattaiprmbtts01scus",
        "westus2":        "exawattaiprmbtts01wus2",
        "redmond":        "exawattaiprmbtts01wus2",
        "rrlab":          "exawattaiprmbtts01wus2",
    }

    if cluster_name in cluster_storage_dict:
        return cluster_storage_dict[cluster_name]
    elif cluster_name.lower() == "ms-shared" or (region is not None):
        return region_storage_dict[region]
    else:
        raise ValueError(
            f"Cannot find the storage account for cluster {cluster_name}")


def get_standard_storage_by_cluster_name(cluster_name, region=None):
    """get associated storage account for a cluster"""

    cluster_storage_dict = {
        "a100-80gb-eus2":   "stdstoragetts01eus",
        "itp-p40-eus-01":   "stdstoragetts01eus",
        "v100-16gb-scus":   "stdstoragetts01scus",
        "a100-scus":        "stdstoragetts01scus",
        "itp-v100-scus":    "stdstoragetts01scus",
        "itp-v100-scus-2":  "stdstoragetts01scus",
        "itp-p100-wus2":    "stdstoragetts01wus2",
        "v100-32gb-wus2-2": "stdstoragetts01wus2",
        "a100-80gb-wus3":   "stdstoragetts01wus2",
        "a100-8x-wus2":     "stdstoragetts01wus2",  # ITP team"s cluster
    }

    region_storage_dict = {
        "eastus":         "stdstoragetts01eus",
        "southcentralus": "stdstoragetts01scus",
        "westus2":        "stdstoragetts01wus2",
        "redmond":        "stdstoragetts01wus2",
        "rrlab":          "stdstoragetts01wus2",
    }

    if cluster_name in cluster_storage_dict:
        return cluster_storage_dict[cluster_name]
    elif cluster_name.lower() == "ms-shared" or (region is not None):
        return region_storage_dict[region]
    else:
        raise ValueError(
            f"Cannot find the storage account for cluster {cluster_name}")


def get_data_storage_by_cluster_name(cluster_name, region=None):
    return get_standard_storage_by_cluster_name(cluster_name, region)


def get_model_storage_by_cluster_name(cluster_name, region=None):
    return get_premium_storage_by_cluster_name(cluster_name, region)


def get_amlt_project_code_storage():
    return "stdstoragetts01scus"


def get_max_sku_by_cluster_name(cluster_name):
    """get max GPU number on a single node for a cluster."""

    cluster_max_sku_dict = {
        "a100-80gb-eus2":   8,
        "itp-p40-eus-01":   4,
        "v100-16gb-scus":   4,
        "a100-scus":        8,
        "itp-v100-scus":    8,
        "itp-v100-scus-2":  4,
        "itp-p100-wus2":    4,
        "v100-32gb-wus2-2": 8,
        "a100-80gb-wus3":   8,
        "a100-8x-wus2":     8,  # ITP team"s cluster
    }

    if cluster_name in cluster_max_sku_dict:
        return cluster_max_sku_dict[cluster_name]
    else:
        raise ValueError(
            f"Cannot find maxsku setting for cluster {cluster_name}")


def is_infiniband_available(cluster_name):
    """check whether the InfiniBand (IB) network is available for a cluster."""

    cluster_infiniband_dict = {
        "a100-80gb-eus2":   True,
        "itp-p40-eus-01":   True,
        "v100-16gb-scus":   True,
        "a100-scus":        True,
        "itp-v100-scus":    True,
        "itp-v100-scus-2":  True,
        "itp-p100-wus2":    True,
        "v100-32gb-wus2-2": True,
        "a100-80gb-wus3":   True,
        "a100-8x-wus2":     True,  # ITP team"s cluster
    }

    if cluster_name in cluster_infiniband_dict:
        return cluster_infiniband_dict[cluster_name]
    else:
        raise ValueError(
            f"Cannot find IB information for cluster {cluster_name}")
