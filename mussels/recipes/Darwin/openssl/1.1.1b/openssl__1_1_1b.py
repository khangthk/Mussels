"""
Copyright (C) 2019 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

from mussels.recipe import BaseRecipe


class Recipe(BaseRecipe):
    """
    Recipe to build libssl.
    """

    name = "openssl"
    version = "1.1.1b"
    url = "https://www.openssl.org/source/openssl-1.1.1b.tar.gz"
    install_paths = {
        "host": {
            "include": [os.path.join("include", "openssl")],
            "lib": [
                os.path.join("libssl.1.1.dylib"),
                os.path.join("libssl.dylib"),
                os.path.join("libssl.a"),
                os.path.join("libcrypto.1.1.dylib"),
                os.path.join("libcrypto.dylib"),
                os.path.join("libcrypto.a"),
            ],
        }
    }
    platform = ["Darwin"]
    dependencies = ["zlib"]
    required_tools = ["make", "clang"]
    build_script = {
        "host": """
            ./config zlib --with-zlib-include="{includes}" --with-zlib-lib="{libs}"
            make
        """
    }
