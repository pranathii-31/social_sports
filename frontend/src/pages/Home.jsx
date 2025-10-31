function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-blue-100 to-blue-300">
      <h1 className="text-4xl font-bold text-blue-800 mb-4">
        Welcome to Social Sports 🏆
      </h1>
      <p className="text-gray-700 text-lg text-center max-w-md">
        Track matches, stats, and players — all in one place.
      </p>
      <button className="mt-6 px-5 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
        Get Started
      </button>
    </div>
  );
}

export default Home;
