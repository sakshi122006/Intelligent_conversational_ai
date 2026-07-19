import React from 'react'

export default function Login() {
  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white/80 p-8 rounded-xl shadow-md w-full max-w-md glass">
        <h1 className="text-2xl font-bold text-policeBlue mb-4">KSP Crime Intelligence</h1>
        <p className="mb-6">Login placeholder (JWT auth to be integrated)</p>
        <button className="w-full bg-policeBlue text-white py-2 rounded">Sign in</button>
      </div>
    </div>
  )
}
