import React from 'react'
import { IoMailOutline } from "react-icons/io5";
import { MdOutlinePhone } from "react-icons/md";
import { LiaFaxSolid } from "react-icons/lia";
import { IoLocationOutline } from "react-icons/io5";

function Contact() {
  return (
    <div className='container mt-4'>
      <div>
        <p><IoMailOutline/> atatepesosyaltesisi@burfas.com.tr</p>
        <p><MdOutlinePhone /> 444 9 444 / 2090 - 0224 800 2090 - 2091- 2092</p>
        <p><LiaFaxSolid /> 0224 800 2077</p>
        <p><IoLocationOutline /> Ata Mahallesi Aydınlar Sokak No:3 Gemlik / Bursa</p>
      </div>
    </div>
  )
}

export default Contact
