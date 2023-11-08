import React from 'react';
import Image from 'next/image';
import test1 from "../../assets/testimonial-1.jpg";
import test2 from "../../assets/testimonial-2.jpg";
import test3 from "../../assets/testimonial-3.jpg";

const Testimonial = () => {
    return (
        <div className="container my-20">
            <div className="text-center">
                <p className="border border-primary-color rounded-full px-4 py-2 w-60 text-center text-xl font-medium">Testimonial</p>
                <h1 className='main-title'>What Say Our Patients!</h1>
            </div>
            <div className="flex">
                <div className="my-8 text-center items-center">
                    <Image className="h-8 w-8 rounded-full border border-primary-color m-4" src={test1} alt='' />
                    <div className="bg-primary-color w-[40vw] p-6 rounded-md">
                        <p className='text-xl font-normal text-font-light mb-4'>Clita clita tempor justo dolor ipsum amet kasd amet duo justo duo duo labore sed sed. Magna ut diam sit et amet stet eos sed clita erat magna elitr erat sit sit erat at rebum justo sea clita.</p>
                        <h5 className="text-xl font-medium text-font-light">Patient Name</h5>
                        <span className="text-xl font-normal text-font-light">Profession</span>
                    </div>
                </div>
                {/* <div className="mt-8 mb-8 text-center">
                    <Image className="h-[8rem] w-[8rem] rounded-full" src={test2} alt='' />
                    <div className="bg-primary-color m-8 p-8 w-[40vw] rounded-es-2xl">
                        <p>Clita clita tempor justo dolor ipsum amet kasd amet duo justo duo duo labore sed sed. Magna ut diam sit et amet stet eos sed clita erat magna elitr erat sit sit erat at rebum justo sea clita.</p>
                        <h5 className="mb-1">Patient Name</h5>
                        <span className="">Profession</span>
                    </div>
                </div>
                <div className="mt-8 mb-8 text-center">
                    <Image className="h-[8rem] w-[8rem] rounded-full" src={test3} alt='' />
                    <div className="bg-primary-color m-8 p-8 w-[40vw] rounded-es-2xl">
                        <p>Clita clita tempor justo dolor ipsum amet kasd amet duo justo duo duo labore sed sed. Magna ut diam sit et amet stet eos sed clita erat magna elitr erat sit sit erat at rebum justo sea clita.</p>
                        <h5 className="mb-1">Patient Name</h5>
                        <span className="">Profession</span>
                    </div>
                </div> */}
            </div>
        </div>
    )
}

export default Testimonial