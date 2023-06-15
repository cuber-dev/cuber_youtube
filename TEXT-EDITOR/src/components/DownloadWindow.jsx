import { useState } from "react"

function DownloadWindow({ content , setIsSubmitted }) {
    const [fileName,setFileName] = useState('newTextFile')
    function handleDownload(e){
        e.preventDefault()
        const a = document.createElement('a')
        const blob = new Blob([content],{ type : 'text/plain'})
        const url = URL.createObjectURL(blob)
        a.href = url
        a.download = `${fileName.replace(".","")}.txt`;
        a.click()
    }
    function handleCancel(){
        setIsSubmitted(false)
    }
    return ( <>
        <div className="outer-container">
            <div className="inner-container">
                <div className="cancel" onClick={handleCancel}>
                    <i className="fa fa-remove" aria-hidden="true"></i>
                </div>
                <h3>Download File</h3>
                <form action="">
                    <label htmlFor="file-name" className="file-name-label">File Name</label>
                    <input 
                    id="file-name"
                    type="text" 
                    className="file-name-input"
                     placeholder="Enter The File Name" 
                     onChange={(e) => setFileName(e.target.value)} />
                    
                    <button 
                    type="submit" 
                    className="btn" 
                    onClick={handleDownload}>
                        Download <i className="fa-solid fa-file-arrow-down" aria-hidden="true"></i></button>
                </form>
            </div>
        </div>
    </> );
}

export default DownloadWindow;
