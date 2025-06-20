// src/components/JobCard.jsx
function JobCard({ empresa, cargo, tags, link }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-4 w-full h-full flex flex-col justify-between">
      <div className="flex justify-between items-start">
        <div>
          <h3 className="text-[#13293D] font-bold text-lg">{empresa}</h3>
          <p className="text-[#247BA0] font-semibold">{cargo}</p>
          <div className="flex flex-wrap gap-2 mt-2">
            {tags?.map((tag, index) => (
              <span
                key={index}
                className="bg-[#1B98E0] text-white text-xs px-3 py-1 rounded-full"
              >
                {tag}
              </span>
            ))}
          </div>
        </div>

        <button
          title="Favoritar"
          className="text-[#13293D] text-xl hover:text-[#1B98E0]"
        >
          ★
        </button>
      </div>

      <div className="flex justify-end gap-2 mt-6">
        <button className="border border-[#13293D] text-[#13293D] font-medium px-3 py-1 rounded-md hover:bg-[#13293D] hover:text-white transition">
          Ver detalhes
        </button>
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="bg-[#006494] text-white font-medium px-3 py-1 rounded-md hover:bg-[#247BA0] transition"
        >
          Acessar vaga
        </a>
      </div>
    </div>
  );
}

export default JobCard;
