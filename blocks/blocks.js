Blockly.defineBlocksWithJsonArray([
{
  "type": "heart_rate_PIN",
  "message0": "Set Heart-rate sensor PIN %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "value",
      "options": [
        [
          "IN1",
          "32"
        ],
        [
          "IN2",
          "33"
        ],
        
        [
          "IN3",
          "34"
        ],
        [
          "IN4",
          "35"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": "#3498DB",
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "push_based",
  "message0": "Data signal heart rate",
  "output": null,
  "colour": "#3498DB",
  "tooltip": "",
  "helpUrl": ""
},

{
  "type": "read_BPM",
  "message0": "Read BPM Setup",
  "previousStatement": null,
  "nextStatement": null,
  "colour": "#3498DB",
  "tooltip": "Setup",
  "helpUrl": ""
},

{
  "type": "heart_rate_bpm",
  "message0": "Heart rate BPM",
  "output": null,
  "colour": "#3498DB",
  "tooltip": "",
  "helpUrl": ""
},

{
  "type": "Detecting_a_beat",
  "message0": "Detecting Heart Beat OUTPUT PIN %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "value",
      "options": [
        [
          "OUT1",
          "26"
        ],
        [
          "OUT2",
          "27"
        ],
        
        [
          "23",
          "23"
        ],
        [
          "19",
          "19"
        ],
        [
          "18",
          "18"
        ],
        [
          "WIFI",
          "2"
        ],
        [
          "IOT",
          "12"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": "#3498DB",
  "tooltip": "",
  "helpUrl": ""
},
]);
