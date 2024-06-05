import React from 'react';
import '../_styles/styles.css';

interface ControlsProps {
  controls: {
    v1xPosition: number;
    v1yPosition: number;
    v1zPosition: number;
    v2xPosition: number;
    v2yPosition: number;
    v2zPosition: number;
    v3xPosition: number;
    v3yPosition: number;
    v3zPosition: number;
    v4xPosition: number;
    v4yPosition: number;
    v4zPosition: number;
    result: string;
  };
}

// Receive vertices of the tetrahedron that was found
const Controls: React.FC<ControlsProps> = ({ controls }) => {
  return (
    <div className="controls">
      <h2>Tetrahedron</h2>
      <div className="controlGroup">
          <h6>Vertex 1</h6>
      </div>
      <div className="controlGroup">
        <div className="control">
          <label>X Position: </label>
          <input
            value={controls.v1xPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Y Position: </label>
          <input
            value={controls.v1yPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Z Position: </label>
          <input
            value={controls.v1zPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
      </div>

      <div className="controlGroup">
          <h6>Vertex 2</h6>
      </div>
      <div className="controlGroup">
        <div className="control">
          <label>X Position: </label>
          <input
            value={controls.v2xPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Y Position: </label>
          <input
            value={controls.v2yPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Z Position: </label>
          <input
            value={controls.v2zPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
      </div>

      <div className="controlGroup">
          <h6>Vertex 3</h6>
      </div>
      <div className="controlGroup">
        <div className="control">
          <label>X Position: </label>
          <input
            value={controls.v3xPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Y Position: </label>
          <input
            value={controls.v3yPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Z Position: </label>
          <input
            value={controls.v3zPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
      </div>

      <div className="controlGroup">
          <h6>Vertex 4</h6>
      </div>
      <div className="controlGroup">
        <div className="control">
          <label>X Position: </label>
          <input
            value={controls.v4xPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Y Position: </label>
          <input
            value={controls.v4yPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
        <div className="control">
          <label>Z Position: </label>
          <input
            value={controls.v4zPosition}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
      </div>

      <div className="controlGroup">
          <h6 style={{color: "cyan"}}>Lines (indexes)</h6>
      </div>
      <div className="controlGroup">
        <div className="control">
          <label>Result: </label>
          <input
            value={controls.result}
            type="text"
            onChange={(e) => (e)}
          />
        </div>
      </div>
    </div>
  );
};

export default Controls;
