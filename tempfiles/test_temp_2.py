def test_tmpdir(tmpdir):
    # Create a temporary file inside the temporary directory
    tmp_file = tmpdir.join("test_file.txt")

    # Write some data to the temporary file
    tmp_file.write("Hello, pytest!")

    # Read the data from the temporary file
    data = tmp_file.read()

    # Assert that the data is what you expect
    assert data == "Hello, pytest!"

    # You can also access the temporary directory path directly
    tmp_dir_path = str(tmpdir)
    assert tmp_file.dirname == tmp_dir_path
