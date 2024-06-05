import pytest

class TestVolumeOfTetrahedron:

    # calculates correct volume for a regular tetrahedron
    def test_calculates_correct_volume_for_regular_tetrahedron(self):
        p1 = np.array([1, 1, 1, 25])
        p2 = np.array([1, -1, -1, 25])
        p3 = np.array([-1, 1, -1, 25])
        p4 = np.array([-1, -1, 1, 25])
        expected_volume = 8 / 6.0
        assert volume_of_tetrahedron(p1, p2, p3, p4) == pytest.approx(expected_volume)

    # handles points that are collinear (volume should be zero)
    def test_handles_collinear_points(self):
        p1 = np.array([0, 0, 0, 25])
        p2 = np.array([1, 1, 1, 25])
        p3 = np.array([2, 2, 2, 25])
        p4 = np.array([3, 3, 3, 25])
        expected_volume = 0.0
        assert volume_of_tetrahedron(p1, p2, p3, p4) == expected_volume

class TestFindSmallestTetrahedron:

    # correctly identifies the smallest tetrahedron from a valid set of points
    def test_correctly_identifies_smallest_tetrahedron(self):
        file_path = 'test_data_valid_points.txt'
        with open(file_path, 'w') as f:
            f.write("0,0,0,25\n1,0,0,25\n0,1,0,25\n0,0,1,25\n1,1,1,50")
        expected_indexes = [0, 1, 2, 3]
        indexes_solution, data = find_smallest_tetrahedron(file_path)
        assert indexes_solution == expected_indexes
        assert data["indexes_solution"] == expected_indexes
        assert data["first_point"] == [0.0, 0.0, 0.0]
        assert data["second_point"] == [1.0, 0.0, 0.0]
        assert data["third_point"] == [0.0, 1.0, 0.0]
        assert data["fourth_point"] == [0.0, 0.0, 1.0]

    # handles input files with fewer than 4 points
    def test_handles_fewer_than_four_points(self):
        file_path = 'test_data_few_points.txt'
        with open(file_path, 'w') as f:
            f.write("0,0,0,25\n1,0,0,25\n0,1,0,25")
        with pytest.raises(ValueError):
            find_smallest_tetrahedron(file_path)