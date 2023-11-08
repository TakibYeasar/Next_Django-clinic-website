import React from 'react';
import Image from 'next/image';
import carousel1 from "../../assets/carousel-1.jpg";
import carousel2 from "../../assets/carousel-2.jpg";
import carousel3 from "../../assets/carousel-3.jpg";

const Banner = () => {
    return (
        <div className="bg-primary-color grid grid-flow-col grid-cols-2 h-screen justify-between">

            <div className="">
                <h1 className="text-7xl font-bold m-8 text-font-light">Good Health Is The Root Of All Heppiness</h1>
                <div className="flex">
                    <div className="items-center m-4">
                        <h2 className="mb-1 text-font-light">123</h2>
                        <p className="mb-0 text-font-light">Expert Doctors</p>
                    </div>
                    <div className="items-center m-4">
                        <h2 className="mb-1 text-font-light">1234</h2>
                        <p className="mb-0 text-font-light">Medical Stuff</p>
                    </div>
                    <div className="items-center m-4">
                        <h2 className="mb-1 text-font-light">12345</h2>
                        <p className="mb-0 text-font-light">Total Patients</p>
                    </div>
                </div>
            </div>

            <div className="">
                <div className="relative items-center justify-center flex">
                    <Image className="h-screen w-[50vw]" src={carousel1} alt="" />

                    <h1 className="absolute top-0 flex items-center justify-center text-font-light text-7xl font-bold mb-0 shadow-sm shadow-font-color">Cardiology</h1>
                </div>
                {/* <div className="relative items-center">
                    <Image className="h-screen w-[50vw]" src={carousel2} alt="" />

                    <h1 className="absolute h-screen w-screen p-12 t-0 l-0 flex items-center justify-center text-font-light text-6xl font-extrabold mb-0">Neurology</h1>
                </div>
                <div className="relative items-center">
                    <Image className="h-screen w-[50vw]" src={carousel3} alt="" />

                    <h1 className="absolute h-screen w-screen p-12 t-0 l-0 flex items-center justify-center text-font-light text-6xl font-extrabold mb-0">Pulmonary</h1>
                </div> */}
            </div>
        </div>
    )
}

export default Banner