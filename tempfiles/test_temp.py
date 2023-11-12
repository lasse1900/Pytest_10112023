def test_tmpfile(tmp_path):
    # Use tmp_path to create a temporary file
    tmp_file = tmp_path / "test_file.txt"

    # Write some data to the temporary file
    tmp_file.write_text("Hello, pytest!")

    # Read the data from the temporary file
    data = tmp_file.read_text()

    # Assert that the data is what you expect
    assert data == "Hello, pytest!"
