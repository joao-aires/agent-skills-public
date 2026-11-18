import { Rpc } from "@opencode/plugin/rpc"

const stateSchema = { type: "object" }

export const Sdlc = Rpc.define({
  id: "sdlc",
  methods: {
    snapshot: {
      input: {
        type: "object",
        properties: { sessionID: { type: "string" } },
        required: ["sessionID"],
        additionalProperties: false,
      },
      output: {
        type: "object",
        properties: { state: stateSchema },
        required: ["state"],
        additionalProperties: false,
      },
    },
    apply: {
      input: {
        type: "object",
        properties: {
          sessionID: { type: "string" },
          command: { type: "object" },
        },
        required: ["sessionID", "command"],
        additionalProperties: false,
      },
      output: {
        type: "object",
        properties: { state: stateSchema },
        required: ["state"],
        additionalProperties: false,
      },
    },
    setAuto: {
      input: {
        type: "object",
        properties: { enabled: { type: "boolean" } },
        required: ["enabled"],
        additionalProperties: false,
      },
      output: {
        type: "object",
        properties: { enabled: { type: "boolean" } },
        required: ["enabled"],
        additionalProperties: false,
      },
    },
  },
  events: {
    updated: {
      schema: {
        type: "object",
        properties: {
          sessionID: { type: "string" },
          state: stateSchema,
        },
        required: ["sessionID", "state"],
        additionalProperties: false,
      },
    },
  },
})
