describe('useFetchPoints', () => {

  // fetchPoints successfully retrieves data and updates state correctly
  it('should update state correctly when fetchPoints successfully retrieves data', async () => {
    const mockResponse = {
      indexes_solution: [1, 2, 3],
      first_point: [0, 0, 0],
      second_point: [1, 1, 1],
      third_point: [2, 2, 2],
      fourth_point: [3, 3, 3],
    };

    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve(mockResponse),
      })
    ) as jest.Mock;

    const { result, waitForNextUpdate } = renderHook(() => useFetchPoints('testFile.txt'));

    act(() => {
      result.current.fetchPoints();
    });

    await waitForNextUpdate();

    expect(result.current.dataPoints).toEqual(mockResponse);
    expect(result.current.isLoading).toBe(false);
    expect(result.current.isError).toBe(false);
  });
});
