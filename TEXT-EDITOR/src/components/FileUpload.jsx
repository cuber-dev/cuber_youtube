

function FileUpload({ setFileContent }) {
    function handleFileUpload(e){
        const file = e.target.files[0]
        if(file){
            const reader = new FileReader()
            reader.onload = () => {
                const result = reader.result
                setFileContent(result)
            }
            reader.onerror = () => {
                alert('Invalid FIle format , Please upload a text file')
                setFileContent('')
                window.location.reload()
            }
            reader.onloadend = () => {
                if (typeof reader.result === 'string' && reader.result.startsWith('data:image')) {
                    // success
                    alert('Dont Upload Folders or binary files. Please upload a Text File.');
                    setFileContent('')
                    window.location.reload()
                }
            };
            reader.readAsText(file)
        }
    }
    return ( <>
        <h1 className="heading">Upload File</h1>
        <input type="file" name="file" id="file" className="file-input" onChange={handleFileUpload}/>
        <label className="file-upload-label" htmlFor="file">Upload File <i className="fa-solid fa-file-arrow-up"></i></label>
    </> );
}

export default FileUpload;