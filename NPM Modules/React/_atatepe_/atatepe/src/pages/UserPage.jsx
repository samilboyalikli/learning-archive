import React from 'react'
import DeskU1 from '../components/desks-for-users/DeskU1'
import DeskU2 from '../components/desks-for-users/DeskU2'
import DeskU3 from '../components/desks-for-users/DeskU3'
import DeskU4 from '../components/desks-for-users/DeskU4'
import DeskU5 from '../components/desks-for-users/DeskU5'
import DeskU6 from '../components/desks-for-users/DeskU6'
import DeskU7 from '../components/desks-for-users/DeskU7'
import DeskU8 from '../components/desks-for-users/DeskU8'
import DeskU9 from '../components/desks-for-users/DeskU9'
import DeskU10 from '../components/desks-for-users/DeskU10'
import DeskU11 from '../components/desks-for-users/DeskU11'
import DeskU12 from '../components/desks-for-users/DeskU12'
import DeskU13 from '../components/desks-for-users/DeskU13'
import DeskU14 from '../components/desks-for-users/DeskU14'
import DeskU15 from '../components/desks-for-users/DeskU15'
import DeskU16 from '../components/desks-for-users/DeskU16'
import DeskU17 from '../components/desks-for-users/DeskU17'
import DeskU18 from '../components/desks-for-users/DeskU18'
import DeskU19 from '../components/desks-for-users/DeskU19'
import DeskU20 from '../components/desks-for-users/DeskU20'
import Rate from '../components/Rate'
import LocationData from '../components/LocationData'

function UserPage() {
    return (
        <div>
            <div className='container'>
                <div className='row mb-5 tb-5'>
                    <div className="col-md-2"><DeskU1/></div>
                    <div className="col-md-2"><DeskU2 /></div>
                    <div className="col-md-2"><DeskU3 /></div>
                    <div className="col-md-2"><DeskU4 /></div>
                    <div className="col-md-2"><DeskU5 /></div>
                </div>
                <div className='row mb-5'>
                    <div className="col-md-2"><DeskU6 /></div>
                    <div className="col-md-2"><DeskU7 /></div>
                    <div className="col-md-2"><DeskU8 /></div>
                    <div className="col-md-2"><DeskU9 /></div>
                    <div className="col-md-2"><DeskU10 /></div>
                </div>
                <div className='row mb-5'>
                    <div className='col-md-2'><DeskU11 /></div>
                    <div className='col-md-2'><DeskU12 /></div>
                    <div className='col-md-2'><DeskU13 /></div>
                    <div className='col-md-2'><DeskU14 /></div>
                    <div className='col-md-2'><DeskU15 /></div>
                </div>
                <div className='row mb-5'>
                    <div className='col-md-2'><DeskU16 /></div>
                    <div className='col-md-2'><DeskU17 /></div>
                    <div className='col-md-2'><DeskU18 /></div>
                    <div className='col-md-2'><DeskU19 /></div>
                    <div className='col-md-2'><DeskU20 /></div>
                </div>            
                <div>
                    <Rate/>
                </div>  
            </div>
        </div>
    )
}

export default UserPage
