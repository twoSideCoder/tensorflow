/* Copyright 2022 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_CC_SAVED_MODEL_FINGERPRINTING_H_
#define TENSORFLOW_CC_SAVED_MODEL_FINGERPRINTING_H_

#include <string>

#include "google/protobuf/map.h"
#include "tensorflow/core/framework/graph.pb.h"
#include "tensorflow/core/platform/types.h"
#include "tensorflow/core/protobuf/fingerprint.pb.h"
#include "tensorflow/core/protobuf/meta_graph.pb.h"

namespace tensorflow::saved_model::fingerprinting {
// Canonicalizes the GraphDef in order to remove sources of non-determinism.
void CanonicalizeGraphDef(GraphDef& graph_def);

// Computes the Fingerprint64 hash of the GraphDef.
uint64 ComputeHash(const GraphDef& graph_def);

// Creates a FingerprintDef proto from a MetaGraph and the checkpoint meta file
// (.index) in `export_dir`.
FingerprintDef CreateFingerprintDef(const MetaGraphDef& metagraph,
                                    absl::string_view export_dir);

}  // namespace tensorflow::saved_model::fingerprinting

#endif  // TENSORFLOW_CC_SAVED_MODEL_FINGERPRINTING_H_
