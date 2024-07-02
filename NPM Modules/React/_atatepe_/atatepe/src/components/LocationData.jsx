import React, { useEffect, useState } from 'react';

function LocationData() {

    const [names, setNames] = useState([]);
    const [images, setImages] = useState([]);

    useEffect(() => {
        fetch('/tesisler.json')
            .then(response => response.json())
            .then(data => {
                const names = data.features.map(feature => feature.properties.ADI);
                setNames(names);
            })
            .catch(error => console.error('Hata:', error));
    }, []);

    return (
        <div>
            {names.map(name => (
                <div className="card mb-3 mt-5" key={name}>
                    <div className="card-body">
                        <h5 className="card-title">{name}</h5>
                    </div>
                </div>
            ))}
        </div>
    );
}



export default LocationData;




