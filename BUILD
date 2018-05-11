# Copyright 2017 The Bazel Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0


py_binary(
    name = "python2",
    srcs = ["Experiment2.py"],
    main = "Experiment2.py",
)

py_test(
    name = "py2_test",
    srcs = ["Experiment2Test.py"],
    main = "Experiment2Test.py",
    deps = ["python2"],
)

py_binary(
    name="python3",
    srcs = ["Experiment3.py"],
    main = "Experiment3.py",
    srcs_version="PY3",
    default_python_version = "PY3",    
)

py_test(
    name="py3_test",
    srcs = ["Experiment3Test.py"],
    main = "Experiment3Test.py",
    srcs_version="PY3",
    default_python_version = "PY3",
    deps = ["python3"],
)

py_binary(
    name="py3_trial",
    srcs = ["trial.py"],
    main = "trial.py",
    srcs_version="PY3",
    default_python_version = "PY3",    
)
