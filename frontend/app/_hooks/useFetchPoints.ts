import { useState } from 'react';

interface DataPoints {
  indexes_solution: number[];
  first_point: number[];
  second_point: number[];
  third_point: number[];
  fourth_point: number[];
}

const useFetchPoints = (fileName: string) => {
  const [dataPoints, setDataPoints] = useState<DataPoints | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isError, setIsError] = useState(false);

  // Rethrieve dataPoints (tetrahedron vertices) on Response
  const fetchPoints = async () => {
    try {
      setIsLoading(true);
      setDataPoints(null);
      const data = { "file_Name": fileName };
      // Switch to Axios on Production :D
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_DEV_URL}/process`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const thedataPoints = await response.json();
      setDataPoints(thedataPoints);
    } catch (error) {
      setIsError(true);
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  // Send interruption process to Flask API to cancel the execution of the tetrahedron search
  const handleCancel = async () => {
    setIsLoading(false);
    setDataPoints(null);
    await fetch(`${process.env.NEXT_PUBLIC_BACKEND_DEV_URL}/cancel`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ cancel: 'true' }),
    });
  };

  // Show small_points.txt or large_points.txt files stored on DynamoDB according to the radio button selected option
  const showDynamoDB = async () => {
    const data = { file_Name: fileName };
    const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_DEV_URL}/dynamo/post`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    if (result.dynamoUpdated === "ok") {
      window.open(`${process.env.NEXT_PUBLIC_BACKEND_DEV_URL}/dynamo/data`, "newwindow");
    }
  };

  return { dataPoints, isLoading, isError, fetchPoints, handleCancel, showDynamoDB  };
};

export default useFetchPoints;