import { Plane, Text } from '@react-three/drei';
import React from 'react';

interface PlaneProps {
  size: number;
}

const XZPlane: React.FC<PlaneProps> = ({ size }) => (
  <Plane args={[size, size, size, size]} rotation={[1.5 * Math.PI, 0, 0]} position={[0, 0, 0]}>
    <meshStandardMaterial attach="material" color="#f9c74f" wireframe />
  </Plane>
);

const XYPlane: React.FC<PlaneProps> = ({ size }) => (
  <Plane args={[size, size, size, size]} rotation={[0, 0, 0]} position={[0, 0, 0]}>
    <meshStandardMaterial attach="material" color="pink" wireframe />
  </Plane>
);

const YZPlane: React.FC<PlaneProps> = ({ size }) => (
  <Plane args={[size, size, size, size]} rotation={[0, Math.PI / 2, 0]} position={[0, 0, 0]}>
    <meshStandardMaterial attach="material" color="#80ffdb" wireframe />
  </Plane>
);

interface GridProps {
  size: number;
}

const Grid: React.FC<GridProps> = ({ size }) => {
  return (
    <group>
      <Text
        color="red"
        anchorX="center"
        anchorY="middle"
        position={[size / 3 + 1, 0, 0]}
        scale={[0.2, 0.2, 0.2]}
      >
        X+
      </Text>
      <Text
        color="red"
        anchorX="center"
        anchorY="middle"
        position={[-size / 3 - 1, 0, 0]}
        scale={[0.2, 0.2, 0.2]}
      >
        X-
      </Text>
      <Text
        color="green"
        anchorX="center"
        anchorY="middle"
        position={[0, size / 3 + 1, 0]}
        scale={[0.2, 0.2, 0.2]}
      >
        Y+
      </Text>
      <Text
        color="green"
        anchorX="center"
        anchorY="middle"
        position={[0, -size / 3 - 1, 0]}
        scale={[0.2, 0.2, 0.2]}
      >
        Y-
      </Text>
      <Text
        color="blue"
        anchorX="center"
        anchorY="middle"
        position={[0, 0, size / 3 + 1]}
        scale={[0.2, 0.2, 0.2]}
      >
        Z+
      </Text>
      <Text
        color="blue"
        anchorX="center"
        anchorY="middle"
        position={[0, 0, -size / 3 - 1]}
        scale={[0.2, 0.2, 0.2]}
      >
        Z-
      </Text>
      <XZPlane size={size} />
      <XYPlane size={size} />
      <YZPlane size={size} />
    </group>
  );
};

export default Grid;
