"use client";
import React, { useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Edges, Polyhedron, PerspectiveCamera } from "@react-three/drei";
import * as THREE from "three";
import Controls from "./_components/Controls";
import Info from "./_components/Info";
import Grid from "./_components/Grid";
import Loading from "./_components/Loading";
import Modal from "./_components/Modal";
import useFetchPoints from "./_hooks/useFetchPoints";
import "./_styles/styles.css";


const HomePage: React.FC = () => {
  // Configure Initial Camera Position
  const cameraSettings = {
    fov: 50,
    position: [400, 400, 400],
    zoom: 100,
    near: 10,
    far: 10000,
  };

  // Modal configs
  const [isModalOpen, setModalOpen] = useState(false);
  const openModal = () => setModalOpen(true);
  const closeModal = () => setModalOpen(false);

  // Imporst hooks
  const [fileName, setFileName] = useState("small");
  const {
    dataPoints,
    isLoading,
    isError,
    fetchPoints,
    handleCancel,
    showDynamoDB,
  } = useFetchPoints(fileName);

  // Setting up the tetrahedron component found from Flask API
  const Tetrahedron: React.FC<{ dataPoints: any }> = ({ dataPoints }) => {
    const vertices = [
      ...dataPoints.first_point,
      ...dataPoints.second_point,
      ...dataPoints.third_point,
      ...dataPoints.fourth_point,
    ];
    const indices = [0, 1, 2, 0, 1, 3, 0, 2, 3, 1, 2, 3];
    return (
      <Polyhedron args={[vertices, indices, 1, 0]}>
        <meshStandardMaterial
          color="red"
          side={THREE.DoubleSide}
          opacity={0.2}
          transparent
        />
        <Edges color="black" />
      </Polyhedron>
    );
  };

  // Handle Generate Tetrahedron
  const renderTetrahedron = (e: React.MouseEvent) => {
    e.preventDefault();
    fetchPoints();
  };

  return (
    <div className="max-w-screen-xlg mx-auto sm:p-5">
      {/* Configure the top right control */}
      <Info />
      <Controls
        controls={{
          v1xPosition: dataPoints ? dataPoints.first_point[0] : 0,
          v1yPosition: dataPoints ? dataPoints.first_point[1] : 0,
          v1zPosition: dataPoints ? dataPoints.first_point[2] : 0,
          v2xPosition: dataPoints ? dataPoints.second_point[0] : 0,
          v2yPosition: dataPoints ? dataPoints.second_point[1] : 0,
          v2zPosition: dataPoints ? dataPoints.second_point[2] : 0,
          v3xPosition: dataPoints ? dataPoints.third_point[0] : 0,
          v3yPosition: dataPoints ? dataPoints.third_point[1] : 0,
          v3zPosition: dataPoints ? dataPoints.third_point[2] : 0,
          v4xPosition: dataPoints ? dataPoints.fourth_point[0] : 0,
          v4yPosition: dataPoints ? dataPoints.fourth_point[1] : 0,
          v4zPosition: dataPoints ? dataPoints.fourth_point[2] : 0,
          result: dataPoints ? `[${dataPoints.indexes_solution.join(', ')}]` : "0"
        }}
      />

      <div className="rounded overflow-hidden flex flex-col mx-auto items-center ">
        {/* <div className="flex flex-row gap-8 justify-center items-center mt-5 mb-5"> */}
        <div className="flex justify-center items-center ">
          <div className="flex flex-wrap gap-2 justify-center max-w-3xl mt-2 mb-2 ">
            {/* Button to call renderTetrahedron */}
            <button
              type="button"
              className="w-[132px] py-2 px-4 flex justify-center items-center text-gray-800 bg-gradient-to-r from-teal-200 to-lime-200 hover:bg-gradient-to-l hover:from-teal-200 hover:to-lime-200 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-teal-700 font-medium rounded-lg text-xs px-5 py-2.5 text-center me-2 mb-2"
              onClick={renderTetrahedron}
            >
              {isLoading ? ( <> <Loading /> Loading ...{" "} </> ) : ( "Generate" )}
            </button>
            {/* Button to clear the graph or cancel the process of finding a tetrahedron */}
            <button
              type="button"
              className="w-[132px] text-white bg-gradient-to-br from-pink-500 to-orange-400 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800 font-medium rounded-lg text-xs px-5 py-2.5 text-center me-2 mb-2"
              onClick={handleCancel}
            >
              Clear/Cancel
            </button>
            {/* Button to view the Flask API of the tetrahdron found */}
            <a href={`${process.env.NEXT_PUBLIC_BACKEND_DEV_URL}/api`} target="_blank">
              <button
                type="button"
                className="w-[132px] text-white bg-gradient-to-br from-gray-300 to-gray-800 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-gray-200 dark:focus:ring-gray-800 font-medium rounded-lg text-xs px-5 py-2.5 text-center me-2 mb-2"
              >
                Flask API
              </button>
            </a>
            {/* Button to view the files stored on DynamoDB: small_points.txt and large_points.txt */}
            <button
              type="button"
              className="w-[132px] text-white bg-gradient-to-r from-cyan-500 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 font-medium rounded-lg text-xs px-5 py-2.5 text-center me-2 mb-2"
              onClick={showDynamoDB}
            >
              DynamoDB
            </button>
            <button
              type="button"
              className="w-[132px] text-gray-900 bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 font-medium rounded-lg text-xs px-5 py-2.5 text-center me-2 mb-2"
              onClick={openModal}
            >
              System Design
            </button>
          </div>
        </div>
      </div>
      <Modal isOpen={isModalOpen} onClose={closeModal} />
      {/* Radio Buttons to specify which file to use or which file should be shown on the API of DynamoDB */}
      <div className="flex flex-wrap gap-x-8 justify-center items-center  ">
        <div>
          <label className="inline-flex items-center" htmlFor="redCheckBox">
            <input
              id="redCheckBox"
              name="radio-item-1"
              type="radio"
              className="w-4 h-4 accent-red-600"
              value="small"
              onChange={(e) => setFileName(e.target.value)}
              defaultChecked={fileName === "small"}
            />
            <span className="ml-2">points_small.txt</span>
          </label>
        </div>
        <div>
          <label className="inline-flex items-center" htmlFor="tealCheckBox">
            <input
              id="tealCheckBox"
              name="radio-item-1"
              type="radio"
              className="w-4 h-4 accent-teal-600"
              value="large"
              onChange={(e) => setFileName(e.target.value)}
              defaultChecked={fileName === "large"}
            />
            <span className="ml-2">points_large.txt</span>
          </label>
        </div>

        {/* Configure the Canvas where the tetrahedron is going to be drawn according to its dataPoints */}
        <div className="flex flex-wrap gap-8 justify-center items-center">
          <div className="w-[90vw] h-[90vh] flex items-start justify-left">
            {/* <Canvas camera={cameraSettings}> */}
            <Canvas>
              <PerspectiveCamera position={[300, 340, 550]} fov={50} zoom={100} near={10} far={10000} makeDefault={true}/>
              <ambientLight intensity={0.5} />
              <pointLight position={[400, 400, 400]} intensity={1} />
              {dataPoints && !isLoading && (
                <Tetrahedron dataPoints={dataPoints} />
              )}
              <OrbitControls />
              <Grid size={5} />
            </Canvas>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
