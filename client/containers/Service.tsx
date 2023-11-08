import React from 'react';
import { FaBrain, FaHeartbeat, FaPlus, FaTooth, FaVials, FaWheelchair, FaXRay } from "react-icons/fa";

const services = [
    {
        title: "Cardiology",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
    {
        title: "Pulmonary",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
    {
        title: "Neurology",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
    {
        title: "Orthopedics",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
    {
        title: "Dental Surgery",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
    {
        title: "Laboratory",
        desc: "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet.",
    },
]

const Service = () => {
    return (
        <div className="container">
            <div className="text-center items-center mb-12">
                <p className="border border-primary-color rounded-full px-4 py-2 w-60 text-center text-xl font-medium">Services</p>
                <h1 className='main-title text-font-color'>Health Care Solutions</h1>
            </div>

            <div className="grid grid-cols-3 gap-4 my-6">
                {services.map((item, i) => (
                    <div className="p-12 rounded-md bg-secondary-color" key={i}>
                        <div className="p-4 bg-bg-color rounded-full w-16">
                            <FaHeartbeat className='text-primary-color text-4xl font-medium ' />
                        </div>
                        <h4 className="text-xl font-semibold my-4">{item?.title}</h4>
                        <p className="text-xl font-normal my-2">{item?.desc}</p>
                        <a className="flex text-xl font-normal my-4 items-center bg-bg-color p-4 no-wrap overflow-hidden transition duration-500 rounded-full" href=""><FaPlus className='text-primary-color mr-4 block group-hover:w-[10rem]' />Read More</a>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Service