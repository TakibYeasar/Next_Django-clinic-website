import React from 'react';
import Image from 'next/image';
import team1 from "../../assets/team-1.jpg";
import team2 from "../../assets/team-2.jpg";
import team3 from "../../assets/team-3.jpg";
import team4 from "../../assets/team-4.jpg";
import { FaFacebook, FaInstagram, FaTwitter } from "react-icons/fa";

const doctors = [
    {
        image: team1,
        name: "Doctor Name",
        dept: "Doctor Department",
    },
    {
        image: team2,
        name: "Doctor Name",
        dept: "Doctor Department",
    },
    {
        image: team3,
        name: "Doctor Name",
        dept: "Doctor Department",
    },
    {
        image: team4,
        name: "Doctor Name",
        dept: "Doctor Department",
    }
]

const Doctors = () => {
    return (
        <div className="container my-20">
            <div className="text-center">
                <p className="border border-primary-color rounded-full px-4 py-2 w-60 text-center text-xl font-medium">Doctors</p>
                <h1 className='main-title'>Our Experience Doctors</h1>
            </div>

            <div className="grid grid-flow-col grid-cols-3 gap-4">
                {doctors.map((item, i) => (
                    <div className="my-8" key={i}>
                            <Image className="top-0 transition duration-500 group-hover/item:t-[-30px]" src={item?.image} alt="" />
                            <div className="transition duration-500 h-28 bg-secondary-color p-4 items-center">
                                <h5 className='text-xl font-medium'>{item?.name}</h5>
                                <p className="text-xl font-normal text-primary-color">{item?.dept}</p>
                                <div className="flex transition duration-500 text-center">
                                    <a className="bg-bg-color p-2 rounded-full m-2" href=""><FaFacebook className='inline-flex text-primary-color text-3xl' /></a>
                                    <a className="bg-bg-color p-2 rounded-full m-2" href=""><FaTwitter className='inline-flex text-primary-color text-3xl' /></a>
                                    <a className="bg-bg-color p-2 rounded-full m-2" href=""><FaInstagram className='inline-flex text-primary-color text-3xl' /></a>
                                </div>
                            </div>
                    </div>
                ))}
            </div>
            
        </div>
    )
}

export default Doctors